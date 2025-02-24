import React from "react";

function About() {
  return (
    <div style={{ padding: "1rem" }}>
      <h2>About Dimension 20 Nexus</h2>
      <p>
        This is an open source project bringing together Dimension 20 data.
      </p>
      <p>
        <strong>GitHub Repo:</strong>{" "}
        <a
          href="https://github.com/orencohendev/dimension20-nexus"
          target="_blank"
          rel="noreferrer"
        >
          dimension20-nexus
        </a>
      </p>
      <p>
        <strong>Twitter:</strong> <a href="https://x.com/theorencohen">@theorencohen</a>
        <br />
        <strong>Threads:</strong> <a href="https://threads.net/@theorencohen">@theorencohen</a>
      </p>
      <p>
        <strong>Contact:</strong>{" "}
        <a href="mailto:oren@geekpeek.blog">oren@geekpeek.blog</a>
      </p>
    </div>
  );
}

export default About;
