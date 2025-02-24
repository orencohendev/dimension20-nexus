import React, { useEffect, useState } from "react";

function Home() {
  // Seasons list
  const [seasons, setSeasons] = useState([]);

  // Which season is selected
  const [selectedSeasonId, setSelectedSeasonId] = useState("");

  // The fetched season info (object)
  const [seasonInfo, setSeasonInfo] = useState(null);

  // The episodes that belong to the selected season
  const [episodes, setEpisodes] = useState([]);

  // The currently chosen episode (entire object, not just ID)
  const [selectedEpisode, setSelectedEpisode] = useState(null);

  // Fetch all seasons on first load
  useEffect(() => {
    fetch("/api/campaigns")
      .then((res) => res.json())
      .then((data) => {
        setSeasons(data);
      })
      .catch((err) => console.error("Error fetching campaigns:", err));
  }, []);

  // Whenever selectedSeasonId changes, fetch that season's details & episodes
  useEffect(() => {
    if (selectedSeasonId) {
      // Fetch the detailed season info
      fetch(`/api/campaigns/${selectedSeasonId}`)
        .then((res) => res.json())
        .then((data) => {
          setSeasonInfo(data);
        })
        .catch((err) => console.error("Error fetching season info:", err));

      // Fetch episodes for that season
      fetch(`/api/campaigns/${selectedSeasonId}/episodes`)
        .then((res) => res.json())
        .then((data) => {
          setEpisodes(data);
          setSelectedEpisode(null); // Reset the episode selection
        })
        .catch((err) => console.error("Error fetching episodes:", err));
    } else {
      setSeasonInfo(null);
      setEpisodes([]);
      setSelectedEpisode(null);
    }
  }, [selectedSeasonId]);

  function handleSeasonChange(e) {
    setSelectedSeasonId(e.target.value);
  }

  // When the user picks an episode, find it in the episodes array
  function handleEpisodeChange(e) {
    const epId = e.target.value;
    const epObject = episodes.find((ep) => ep.id === epId);
    setSelectedEpisode(epObject || null);
  }

  return (
    <div style={styles.container}>
      <h2>Select a Season</h2>
      <select onChange={handleSeasonChange} value={selectedSeasonId}>
        <option value="">-- Choose a season --</option>
        {seasons.map((season) => (
          <option key={season.id} value={season.id}>
            {season.title}
          </option>
        ))}
      </select>

      {/* Show campaign info (title, url, description, year, reviews) */}
      {seasonInfo && (
        <div style={styles.infoBox}>
          <h3>{seasonInfo.title}</h3>
          <p>
            <strong>Year:</strong> {seasonInfo.year}
          </p>
          <p>
            <strong>Description:</strong> {seasonInfo.description}
          </p>
          {seasonInfo.url && (
            <p>
              <strong>Link:</strong>{" "}
              <a href={seasonInfo.url} target="_blank" rel="noreferrer">
                {seasonInfo.url}
              </a>
            </p>
          )}

          {/* Reviews Section */}
          {seasonInfo.reviews && seasonInfo.reviews.length > 0 && (
            <>
              <h4>Reviews:</h4>
              <ul style={{ listStyle: "none", paddingLeft: 0 }}>
                {seasonInfo.reviews.map((review) => (
                  <li key={review.id} style={styles.reviewItem}>
                    <strong>{review.source}</strong>
                    <br />
                    <a href={review.url} target="_blank" rel="noreferrer">
                      {review.url}
                    </a>
                    <p>{review.excerpt}</p>
                    <p>
                      <em>Rating:</em> {review.rating}
                    </p>
                  </li>
                ))}
              </ul>
            </>
          )}
        </div>
      )}

      <h2>Select an Episode</h2>
      <select
        onChange={handleEpisodeChange}
        value={selectedEpisode?.id || ""}
        disabled={!episodes.length}
      >
        <option value="">-- Choose an episode --</option>
        {episodes.map((ep) => (
          <option key={ep.id} value={ep.id}>
            {ep.title}
          </option>
        ))}
      </select>

      {/* Show selected episode's details */}
      {selectedEpisode && (
        <div style={styles.infoBox}>
          <h4>{selectedEpisode.title}</h4>
          <p>
            <strong>Episode Number:</strong> {selectedEpisode.episode_number}
          </p>
          <p>
            <strong>Air Date:</strong> {selectedEpisode.air_date}
          </p>
          <p>
            <strong>Description:</strong> {selectedEpisode.description}
          </p>
          {selectedEpisode.url && (
            <p>
              <strong>Link:</strong>{" "}
              <a href={selectedEpisode.url} target="_blank" rel="noreferrer">
                Watch Here
              </a>
            </p>
          )}
        </div>
      )}
    </div>
  );
}

const styles = {
  container: {
    padding: "1rem",
  },
  infoBox: {
    border: "1px solid #ccc",
    padding: "1rem",
    marginTop: "1rem",
  },
  reviewItem: {
    marginBottom: "1rem",
    padding: "0.5rem",
    border: "1px dashed #ccc",
  },
};

export default Home;
