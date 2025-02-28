// src/pages/Home.tsx
import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import {
  Box,
  Container,
  Typography,
  Button,
  Card,
  CardContent,
  List,
  ListItem,
  ListItemText,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Link
} from '@mui/material'

interface Review {
  id: string
  source: string
  url: string
  excerpt: string
  rating: number
}

interface Campaign {
  id: string
  title: string
  url: string
  description: string
  year: number
  reviews: Review[]
}

interface Episode {
  id: string
  campaign_id: string
  title: string
  episode_number: number
  url: string
  air_date: string
  description: string
}

const Home: React.FC = () => {
  const { campaignSlug } = useParams<{ campaignSlug?: string }>()
  const [campaigns, setCampaigns] = useState<Campaign[]>([])
  const [selectedCampaignId, setSelectedCampaignId] = useState<string>('')
  const [campaignInfo, setCampaignInfo] = useState<Campaign | null>(null)
  const [episodes, setEpisodes] = useState<Episode[]>([])
  const [selectedEpisode, setSelectedEpisode] = useState<Episode | null>(null)

  // Convert a campaign title to a "slug"
  const computeSlug = (title: string): string =>
    title.toLowerCase().trim().replace(/\s+/g, '-')

  // Fetch all campaigns on mount
  useEffect(() => {
    fetch('/api/campaigns')
      .then((res) => res.json())
      .then((data: Campaign[]) => {
        setCampaigns(data)
        if (campaignSlug) {
          const matched = data.find(
            (c) => computeSlug(c.title) === campaignSlug.toLowerCase()
          )
          if (matched) {
            setSelectedCampaignId(matched.id)
          }
        }
      })
      .catch((err) => console.error('Error fetching campaigns:', err))
  }, [campaignSlug])

  // When selectedCampaignId changes, fetch campaign details & episodes
  useEffect(() => {
    if (selectedCampaignId) {
      fetch(`/api/campaigns/${selectedCampaignId}`)
        .then((res) => res.json())
        .then((data: Campaign) => setCampaignInfo(data))
        .catch((err) => console.error('Error fetching campaign info:', err))

      fetch(`/api/campaigns/${selectedCampaignId}/episodes`)
        .then((res) => res.json())
        .then((data: Episode[]) => {
          setEpisodes(data)
          setSelectedEpisode(null)
        })
        .catch((err) => console.error('Error fetching episodes:', err))
    } else {
      setCampaignInfo(null)
      setEpisodes([])
      setSelectedEpisode(null)
    }
  }, [selectedCampaignId])

  const handleCampaignChange = (e: React.ChangeEvent<{ value: unknown }>) => {
    setSelectedCampaignId(e.target.value as string)
  }

  const handleEpisodeChange = (e: React.ChangeEvent<{ value: unknown }>) => {
    const epId = e.target.value as string
    const ep = episodes.find((episode) => episode.id === epId)
    setSelectedEpisode(ep || null)
  }

  return (
    <>
      {/* Full-width hero section */}
      <Box sx={{ width: '100%', backgroundColor: '#f5f5f5', py: 4 }}>
        <Container maxWidth="md" sx={{ textAlign: 'center' }}>
          <Typography variant="h3" gutterBottom>
            Dimension 20 Nexus
          </Typography>
          <Typography variant="h6" color="text.secondary" gutterBottom>
            A free, open-source resource for Dimension 20 data
          </Typography>
          <Box sx={{ mt: 2 }}>
            <Button variant="contained" color="primary" href="/api/docs" target="_blank" sx={{ mr: 2 }}>
              API Docs
            </Button>
            <Button variant="outlined" color="primary" href="https://github.com/orencohendev/dimension20-nexus" target="_blank">
              Contribute on GitHub
            </Button>
          </Box>
        </Container>
      </Box>

      {/* Main container for the rest of the content */}
      <Container maxWidth="md" sx={{ textAlign: 'center', py: 4 }}>
        {/* Infographic / Bulleted Highlights */}
        <Card sx={{ mb: 4, width: '100%' }}>
          <CardContent>
            <Typography variant="h5" gutterBottom>
              What You Should Know
            </Typography>
            <List>
              <ListItem>
                <ListItemText
                  primary="What is Dimension 20 Nexus?"
                  secondary="A community-driven project that centralizes Dimension 20 data—campaigns, episodes, reviews, and more—in one place."
                />
              </ListItem>
              <ListItem>
                <ListItemText
                  primary="Why an API?"
                  secondary="It provides structured data so you can build apps, bots, or websites without scraping the web."
                />
              </ListItem>
              <ListItem>
                <ListItemText
                  primary="How You Can Use It"
                  secondary="Dive into our docs, fetch JSON from our endpoints, or fork the code to contribute improvements."
                />
              </ListItem>
              <ListItem>
                <ListItemText
                  primary="Why We're Proud"
                  secondary="We built a resource that sparks creative ideas—even if it remains a niche tool."
                />
              </ListItem>
            </List>
          </CardContent>
        </Card>

        {/* Campaign Selection Section */}
        <Card sx={{ mb: 4, width: '100%' }}>
          <CardContent>
            <Typography variant="h5" gutterBottom>
              Explore Campaigns
            </Typography>
            <FormControl fullWidth sx={{ mt: 2 }}>
              <InputLabel id="campaign-select-label">Campaign</InputLabel>
              <Select
                labelId="campaign-select-label"
                id="campaign-select"
                value={selectedCampaignId}
                label="Campaign"
                onChange={handleCampaignChange}
              >
                <MenuItem value="">
                  <em>None</em>
                </MenuItem>
                {campaigns.map((campaign) => (
                  <MenuItem key={campaign.id} value={campaign.id}>
                    {campaign.title}
                  </MenuItem>
                ))}
              </Select>
            </FormControl>
          </CardContent>
        </Card>

        {/* Campaign Details */}
        {campaignInfo && (
          <Card sx={{ mb: 4, width: '100%' }}>
            <CardContent>
              <Typography variant="h5">{campaignInfo.title}</Typography>
              <Typography variant="subtitle1" color="text.secondary">
                {campaignInfo.year}
              </Typography>
              <Typography variant="body1" sx={{ mt: 1 }}>
                {campaignInfo.description}
              </Typography>
              {campaignInfo.url && (
                <Typography variant="body2" sx={{ mt: 1 }}>
                  <strong>Link:</strong>{' '}
                  <Link href={campaignInfo.url} target="_blank" rel="noopener">
                    Visit Campaign Page
                  </Link>
                </Typography>
              )}
              {campaignInfo.reviews && campaignInfo.reviews.length > 0 && (
                <Box sx={{ mt: 2 }}>
                  <Typography variant="h6">Reviews</Typography>
                  {campaignInfo.reviews.map((review) => (
                    <Box key={review.id} sx={{ border: '1px dashed #ccc', p: 1, mb: 1, borderRadius: 1 }}>
                      <Typography variant="subtitle2">{review.source}</Typography>
                      <Typography variant="body2">
                        <Link href={review.url} target="_blank" rel="noopener">
                          {review.url}
                        </Link>
                      </Typography>
                      <Typography variant="body2">{review.excerpt}</Typography>
                      <Typography variant="caption">Rating: {review.rating}</Typography>
                    </Box>
                  ))}
                </Box>
              )}
            </CardContent>
          </Card>
        )}

        {/* Episode Selection Section */}
        {campaignInfo && (
          <Card sx={{ mb: 4, width: '100%' }}>
            <CardContent>
              <Typography variant="h5" gutterBottom>
                Episodes
              </Typography>
              <FormControl fullWidth sx={{ mt: 2 }}>
                <InputLabel id="episode-select-label">Episode</InputLabel>
                <Select
                  labelId="episode-select-label"
                  id="episode-select"
                  value={selectedEpisode ? selectedEpisode.id : ''}
                  label="Episode"
                  onChange={handleEpisodeChange}
                  disabled={episodes.length === 0}
                >
                  <MenuItem value="">
                    <em>None</em>
                  </MenuItem>
                  {episodes.map((ep) => (
                    <MenuItem key={ep.id} value={ep.id}>
                      {ep.title}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>

              {selectedEpisode && (
                <Box sx={{ mt: 3 }}>
                  <Typography variant="h6">{selectedEpisode.title}</Typography>
                  <Typography variant="subtitle1" color="text.secondary">
                    Episode {selectedEpisode.episode_number} - {selectedEpisode.air_date}
                  </Typography>
                  <Typography variant="body1" sx={{ mt: 1 }}>
                    {selectedEpisode.description}
                  </Typography>
                  {selectedEpisode.url && (
                    <Typography variant="body2" sx={{ mt: 1 }}>
                      <Link href={selectedEpisode.url} target="_blank" rel="noopener">
                        Watch Episode
                      </Link>
                    </Typography>
                  )}
                </Box>
              )}
            </CardContent>
          </Card>
        )}
      </Container>
    </>
  )
}

export default Home
