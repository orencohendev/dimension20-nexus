// src/App.tsx
import React from 'react'
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'
import { AppBar, Toolbar, Typography, Button } from '@mui/material'
import Home from './pages/Home'
import About from './pages/About'

const App: React.FC = () => {
  return (
    <Router>
      {/* Full-width header at the top */}
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1 }}>
            Dimension 20 Nexus
          </Typography>
          <Button color="inherit" component={Link} to="/">Home</Button>
          <Button color="inherit" component={Link} to="/about">About</Button>
        </Toolbar>
      </AppBar>

      {/* Main content routes */}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/campaigns/:campaignSlug" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Router>
  )
}

export default App
