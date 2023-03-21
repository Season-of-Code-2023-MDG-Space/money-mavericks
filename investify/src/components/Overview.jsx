import React from 'react';
import PortfolioCard from './PortfolioCard';
import Table from './Table';
import data1 from '../assets/data/data1';
import data2 from '../assets/data/data2';
import data3 from '../assets/data/data3';
import data4 from '../assets/data/data4';

function Overview() {
  return (
    <div>
     <div className="container">
              <PortfolioCard/>
              </div>
               
              <div className="container2">
                <div className="table-grid">
                  <div className="table-column">
                    <Table headers={['Share', 'Price', 'Change','Percent']} data={data1} heading="MY PORTFOLIO"/>
                  </div>
                  <div className="table-column">
                    <Table headers={['Share', 'Close', 'Volume']} data={data2} heading="MOST  TRANSCATIONS " />
                  </div>
                  <div className="table-column">
                    <Table headers={['Share', 'Close', 'Percent']} data={data3} heading="MOST INCREASED"/>
                  </div>
                  <div className="table-column">
                    <Table headers={['Share', 'Close', 'Percent']} data={data4} heading="MOST REDUCED" />
                  </div>
                </div>
          
                
              </div>
    </div>
  )
}

export default Overview