// src/pages/About.tsx
import React from 'react'
import { Container, Typography, Box, Link } from '@mui/material'

const About: React.FC = () => {
  return (
    <Container maxWidth="md" sx={{ py: 4, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
      <Box sx={{ textAlign: 'center', mb: 4, width: '100%' }}>
        <Typography variant="h3" gutterBottom>
          About Dimension 20 Nexus
        </Typography>
        <Typography variant="body1">
          Dimension 20 Nexus is an open‑source project that aggregates data about Dimension 20 campaigns, episodes, reviews, and more.
          This platform provides a free API for developers and creators, making it easy to integrate Dimension 20 data into your own applications without the hassle of web scraping.
        </Typography>
      </Box>
      <Box sx={{ textAlign: 'center' }}>
        <Typography variant="h6">Get in Touch</Typography>
        <Typography variant="body2">
          Follow us on{' '}
          <Link href="https://x.com/@theorencohen" target="_blank" rel="noopener">
            Twitter
          </Link>{' '}
          /{' '}
          <Link href="https://threads.net/@theorencohen" target="_blank" rel="noopener">
            Threads
          </Link>{' '}
          or visit our{' '}
          <Link href="https://github.com/orencohendev/dimension20-nexus" target="_blank" rel="noopener">
            GitHub Repo
          </Link>.
        </Typography>
        <Typography variant="body2" sx={{ mt: 1 }}>
          For questions or feedback, email:{' '}
          <Link href="mailto:oren@geekpeek.blog">oren@geekpeek.blog</Link>
        </Typography>
      </Box>
    </Container>
  )
}

export default About
