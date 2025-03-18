// src/App.tsx
import React, { useEffect } from 'react'
import { BrowserRouter as Router, Routes, Route, useLocation, Link } from 'react-router-dom'
import ReactGA from 'react-ga4'
import { AppBar, Toolbar, Typography, Button } from '@mui/material'
import Home from './pages/Home'
import About from './pages/About'

// Initialize react-ga4 with your GA4 Measurement ID
ReactGA.initialize('G-G5KJRESKTS') // Replace with your actual GA4 ID

// Analytics component: sends a pageview on route changes
const Analytics: React.FC = () => {
  const location = useLocation()
  useEffect(() => {
    ReactGA.send({ hitType: 'pageview', page: location.pathname + location.search })
  }, [location])
  return null
}

const App: React.FC = () => {
  return (
    <Router>
      <Analytics />
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1 }}>
            Dimension 20 Nexus
          </Typography>
          <Button color="inherit" component={Link} to="/">Home</Button>
          <Button color="inherit" component={Link} to="/about">About</Button>
        </Toolbar>
      </AppBar>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/:campaignSlug" element={<Home />} />
        <Route path="/:campaignSlug/:episodeSlug" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Router>
  )
}

export default App
