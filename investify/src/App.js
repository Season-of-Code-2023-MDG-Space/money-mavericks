import React from 'react';
import './App.css'
import SideMenu from './components/SideMenu';
import Navbar from './components/Navbar';
import Overview from './components/Overview';
import ChatBot from './components/ChatBot';
import UserDataCard from './components/UserDataCard';
import DetailsCard from './components/DetailsCard';
import detailsData from './assets/data/data';
import LoginPage from './components/login';
import StockNameInputForm from './components/StockNameInputForm';
import MultiLineChart from './LineGraph';
import {
  BrowserRouter as Router,
  Routes,
  Route
} from "react-router-dom";

function App() {

  return (
    <>
    <Navbar/>
    <SideMenu />
    <Router>
      <Routes>
        <Route path="/Overview" element={<Overview />} />
        <Route path="/" element={<LoginPage/>} />
        <Route path="/Pricechart" element={<MultiLineChart />} />
        <Route path="/PricePredict" element={<StockNameInputForm/>} />
        <Route path="/ChatBot" element={<ChatBot/>} />
        <Route path="/MyAccount" element={<UserDataCard
        username="JDoe"
        name="John Doe"
        balance="$123456.78"
        holdings="GOOG:78 APPL:15"
        profit="$123.45"
        loss="$234.56"
      />} />
      <Route path="/MyTransacHistory" element={ <div className="container">
       <div className="details-card-container">
      {detailsData.map((data, index) => (
        <DetailsCard key={index} data={data} />
      ))}
    </div>
    </div>} />
      </Routes>
    </Router>
    </> 
  );
}

export default App;

