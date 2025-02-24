import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import About from "./pages/About";
import "./App.css";

function App() {
  return (
    <Router>
      <div style={styles.container}>
        <header style={styles.header}>
          <h1 style={styles.title}>Dimension 20 Nexus</h1>
          <nav>
            <Link style={styles.link} to="/">Home</Link>
            <Link style={styles.link} to="/about">About</Link>
          </nav>
        </header>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </div>
    </Router>
  );
}

const styles = {
  container: {
    fontFamily: "sans-serif",
    minHeight: "100vh",
    backgroundColor: "#fafafa"
  },
  header: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "1rem",
    backgroundColor: "#eee"
  },
  title: {
    margin: 0
  },
  link: {
    marginRight: "1rem",
    textDecoration: "none",
    fontWeight: "bold"
  }
};

export default App;
