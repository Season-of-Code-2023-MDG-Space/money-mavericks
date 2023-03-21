import React from 'react';
import "../styles/PortfolioCard.css"

function PortfolioCard({ title, text }) {
  return (
    <div className="text-card">
        <h2>Portfolio(Total)</h2>
      <div className="cardcontainer">
  <div className="item">$9,844.88</div>
  <div className="item">Daily Return</div>
  <div className="item">Total Return</div>
  <div className="item"> </div>
  <div className="item green">+146.34(+1.51%)</div>
  <div className="item red">+1,756.28(+21.72%)</div>
</div>

    </div>
  );
}

export default PortfolioCard;
