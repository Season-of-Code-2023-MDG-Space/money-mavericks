import React from 'react';
import '../styles/Navbar.css';

function Navbar() {
  return (
    <div className="navbar">
      <div className="navbar-logo">
      </div>
      <div className="navbar-search">
        <input type="text" placeholder="Search..." />
        <i className="fas fa-search"></i>
      </div>
      <div className="navbar-right">
        <div className="navbar-caption">
          <h5>Welcome, John Doe</h5>
        </div>
        <div className="navbar-login">
          <i className="fas fa-user"></i>
          <h5><a href='/login'>Login</a></h5>
        </div>
      </div>
    </div>
  );
}

export default Navbar;
