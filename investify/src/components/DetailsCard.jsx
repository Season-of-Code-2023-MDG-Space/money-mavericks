import React from 'react';
import '../styles/DetailsCard.css';

function DetailsCard(props ) {
  return (
    <div className="details-card">
      <div className="details-card-header">{props.data.StockName}</div>
      <div className="details-card-body">
        <div className="details-card-item">
          <div className="details-card-label">Quantity Holding:</div>
          <div className="details-card-value">{props.data.QuantityHolding}</div>
        </div>
        <div className="details-card-item">
          <div className="details-card-label">Purchased Price:</div>
          <div className="details-card-value">${props.data.PurchasedPrice}</div>
        </div>
        <div className="details-card-item">
          <div className="details-card-label">Sold Price:</div>
          <div className="details-card-value">${props.data.SoldPrice}</div>
        </div>
        <div className="details-card-item">
          <div className="details-card-label">Purchasing Date:</div>
          <div className="details-card-value">{props.data.PurchasingDate}</div>
        </div>
        <div className="details-card-item">
          <div className="details-card-label">Selling Date:</div>
          <div className="details-card-value">{props.data.SellingDate}</div>
        </div>
      </div>
    </div>
  );
}

export default DetailsCard;
