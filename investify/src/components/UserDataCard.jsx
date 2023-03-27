import React from 'react';
import '../styles/UserDataCard.css'; 
import avatar from '../assets/images/user.png'

function UserDataCard(props) {
  return (
    <div className="container3">
    <div className="user-data-card">
      <img className="user-avatar" src={avatar} alt="user avatar"/>
      <div className="user-details">
        <h2 className="user-username">{props.username}</h2>
        <p className="user-name">{props.name}</p>
        <p className="user-balance">Balance:{props.balance}</p>
        <p className="user-holdings">Holdings: {props.holdings}</p>
        <p className="user-profit green"> Profit:{props.profit}</p>
        <p className="user-loss red">Loss: {props.loss}</p>
      </div>
    </div>
    </div>
  );
}

export default UserDataCard;
