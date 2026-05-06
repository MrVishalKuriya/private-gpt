# PrivateGPT — Frontend (React + Vite)

This is the React-based user interface for the PrivateGPT platform.

## 🚀 Getting Started

1. **Install Dependencies**:
   ```bash
   npm install
   ```

2. **Configuration**:
   Create a `.env` file in the `frontend` root:
   ```env
   VITE_API_URL=http://localhost:8000/api/v1
   ```

3. **Development Server**:
   ```bash
   npm run dev
   ```

## 🏗️ Tech Stack

- **Framework**: [React](https://reactjs.org/) (with [Vite](https://vitejs.dev/))
- **Styling**: [TailwindCSS](https://tailwindcss.com/)
- **Animations**: [Framer Motion](https://www.framer.com/motion/)
- **Icons**: [Lucide React](https://lucide.dev/)
- **Routing**: [React Router](https://reactrouter.com/)
- **API Client**: [Axios](https://axios-http.com/)

## 📁 Key Directories

- `src/context/`: Authentication and Global State.
- `src/pages/`: Main views (Login, Signup, PrivateGPT Dashboard).
- `src/components/`: Reusable UI elements (Navbar, Modals, etc.).
- `src/utils/`: AI utilities, file processing, and API helpers.

## 🔒 Feature Highlights

- **Streaming Responses**: Real-time "typing" effect for AI answers.
- **Offline-First Previews**: Documents are processed locally for instant viewing.
- **Note-taking**: Users can save AI responses to a persistent notebook.
- **Responsive Design**: Fully optimized for mobile and desktop screens.
