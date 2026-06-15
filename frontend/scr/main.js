cat > src/main.js << 'EOF'
// Import any CSS if needed
// import './style.css'

// Create content for the app
document.getElementById('app').innerHTML = `
  <div style="text-align: center; padding: 50px; font-family: Arial, sans-serif;">
    <h1>🎉 Welcome to Your Frontend App!</h1>
    <p>Your Vite dev server is running successfully.</p>
    <p>src/main.js is now loaded!</p>
    <button onclick="alert('Hello from JavaScript!')">Click Me</button>
  </div>
`;

console.log('App is running!');
EOF