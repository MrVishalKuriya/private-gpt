import { createContext, useContext, useState } from 'react';

const AuthContext = createContext(null);

// eslint-disable-next-line react-refresh/only-export-components
export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(() => {
    const stored = typeof window !== 'undefined' ? localStorage.getItem('regenesys_user') : null;
    if (stored) {
      try {
        return JSON.parse(stored);
      } catch {
        localStorage.removeItem('regenesys_user');
      }
    }
  });

  const [aiSidebarOpen, setAiSidebarOpen] = useState(false);

  const API_BASE_URL = 'http://localhost:8000/api/v1';

  const signup = async (name, email, password) => {
    try {
      const response = await fetch(`${API_BASE_URL}/auth/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password, full_name: name }),
      });

      const data = await response.json();

      if (!response.ok) {
        return { success: false, error: data.detail || 'Signup failed' };
      }

      // After signup, we log them in automatically
      return await login(email, password);
    } catch (error) {
      return { success: false, error: 'Connection to server failed' };
    }
  };

  const login = async (email, password) => {
    try {
      const formData = new FormData();
      formData.append('username', email);
      formData.append('password', password);

      const response = await fetch(`${API_BASE_URL}/auth/login`, {
        method: 'POST',
        body: formData, // OAuth2PasswordRequestForm expects form-data
      });

      const data = await response.json();

      if (!response.ok) {
        return { success: false, error: data.detail || 'Login failed' };
      }

      // Get user profile info after login
      const profileResponse = await fetch(`${API_BASE_URL}/profile/me`, {
        headers: { 'Authorization': `Bearer ${data.access_token}` },
      });
      const profileData = await profileResponse.json();

      const sessionUser = {
        ...profileData,
        token: data.access_token,
        refreshToken: data.refresh_token,
        avatar: (profileData.full_name || email).split(' ').map(n => n[0]).join('').toUpperCase().slice(0, 2)
      };

      setUser(sessionUser);
      localStorage.setItem('regenesys_user', JSON.stringify(sessionUser));

      return { success: true };
    } catch (error) {
      return { success: false, error: 'Connection to server failed' };
    }
  };

  const logout = async () => {
    try {
      if (user?.token) {
        await fetch(`${API_BASE_URL}/auth/logout`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${user.token}`
          },
          body: JSON.stringify({ refresh_token: user.refreshToken }),
        });
      }
    } catch (e) {
      console.error('Logout error:', e);
    } finally {
      setUser(null);
      localStorage.removeItem('regenesys_user');
    }
  };

  return (
    <AuthContext.Provider value={{ user, login, signup, logout, aiSidebarOpen, setAiSidebarOpen, checkEmail }}>
      {children}
    </AuthContext.Provider>
  );
};
