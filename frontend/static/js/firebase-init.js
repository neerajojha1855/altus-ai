import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAuth, GoogleAuthProvider, signInWithPopup, createUserWithEmailAndPassword, signInWithEmailAndPassword, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

// Read from injected window.env
const firebaseConfig = {
    apiKey: window.env.FIREBASE_API_KEY,
    authDomain: window.env.FIREBASE_AUTH_DOMAIN,
    projectId: window.env.FIREBASE_PROJECT_ID,
    storageBucket: window.env.FIREBASE_PROJECT_ID + ".appspot.com",
    messagingSenderId: "",
    appId: ""
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();

// Expose to window for inline scripts
window.firebaseAuth = auth;
window.GoogleAuthProvider = GoogleAuthProvider;
window.firebaseProvider = provider;
window.signInWithPopup = signInWithPopup;
window.createUserWithEmailAndPassword = createUserWithEmailAndPassword;
window.signInWithEmailAndPassword = signInWithEmailAndPassword;

let currentUser = null;

function updateNavbar() {
    const navUnauth = document.getElementById('nav-unauth');
    const navAuth = document.getElementById('nav-auth');
    if (currentUser) {
        if (navUnauth) navUnauth.classList.add('hidden');
        if (navAuth) navAuth.classList.remove('hidden');
    } else {
        if (navUnauth) navUnauth.classList.remove('hidden');
        if (navAuth) navAuth.classList.add('hidden');
    }
}

// Handle Auth state changes and token storage
onAuthStateChanged(auth, (user) => {
    currentUser = user;
    if (user) {
        user.getIdToken().then((token) => {
            localStorage.setItem("firebaseToken", token);
        });
        
        // Auto-redirect to dashboard if on login/home page
        if (window.location.pathname === '/' || window.location.pathname === '/login') {
            window.location.href = '/dashboard';
        }
    } else {
        localStorage.removeItem("firebaseToken");
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', updateNavbar);
    } else {
        updateNavbar();
    }
});

// Attach logout handler if button exists
document.addEventListener('DOMContentLoaded', () => {
    const logoutBtn = document.getElementById('logout-btn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', async () => {
            try {
                await auth.signOut();
                window.location.href = "/";
            } catch (error) {
                console.error("Logout error", error);
            }
        });
    }
});
