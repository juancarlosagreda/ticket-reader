
import React, { useState, useEffect, useRef } from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCashRegister, faChartLine, faCloudUploadAlt, faPlus, faRocket, faTasks, faUserShield } from '@fortawesome/free-solid-svg-icons';
import { Col, Row, Button, Dropdown, ButtonGroup } from '@themesberg/react-bootstrap';

import { CounterWidget, CircleChartWidget, BarChartWidget, TeamMembersWidget, ProgressTrackWidget, RankingWidget, SalesValueWidget, SalesValueWidgetPhone, AcquisitionWidget } from "../components/Widgets";
import { PageVisitsTable } from "../components/Tables";
import { trafficShares, totalOrders } from "../data/charts";


import axios from 'axios'

// import firebase config data
import config from "../data/config"

// Firebase App (the core Firebase SDK) is always required and must be listed first
import firebase from "firebase/app";

// Add the Firebase products that you want to use
import "firebase/storage";
import "firebase/firestore";

// Initialize Firebase
if (!firebase.apps.length) {
  firebase.initializeApp(config);
} else {
  firebase.app(); // if already initialized, use that one
}

// Get a reference to the storage service, which is used to create references in your storage bucket
var storage = firebase.storage();

// Get a reference to the storage service, which is used to create references in your storage bucket
var firestore = firebase.firestore();


export default () => {

  const [netWorth, setNetWorth] = useState('');
  const [path, setPath] = useState('');
  const [isDisabled, setIsDisabled] = useState(true);

  const baseURL = '/Users/JuanCarlos/ticket-reader/server/Imagenes/';


  const fileInput = useRef(null)


  const handleClick = (e) => {
    e.preventDefault();
    console.log(fileInput.current);
    fileInput.current.click();
  }

  const fileSelectedHandler = e => {
    console.log(e.target.files[0]);
    setPath(baseURL + e.target.files[0].name)
    setIsDisabled(false)
  }

  const fileUploadHandler = () => {
    console.log("path sent: " + path)

    if (path !== "") {
      axios.post('http://localhost:8081/add', path, {
        headers: { 'Content-Type': 'text/plain' }
      }).then(res => {
        console.log(res);
      });
    }
    //   axios({
    //     method: 'get',
    //     url: 'http://localhost:8080/add',
    //     headers: {},
    //     data: path
    //   }).then(res => {
    //     console.log(res)
    //   });
  }

  useEffect(() => {
    axios.get('http://localhost:8081/netValue')
      .then((response) => {
        console.log(response.data.netValue)
        setNetWorth(response.data.netValue)
      })
  }, [])

  return (
    <>
      <div className="d-flex flex-wrap flex-md-nowrap align-items-center py-4">
        <input onChange={fileSelectedHandler} type="file" ref={fileInput} style={{ display: 'none' }} />
        <Button variant="primary" onClick={handleClick} className="m-1">
          <FontAwesomeIcon icon={faPlus} className="me-2" />New Ticket
          </Button>
        <Button variant="primary" className="m-1">
          <FontAwesomeIcon onClick={fileUploadHandler()} icon={faCloudUploadAlt} className="me-2" /> Upload Ticket
        </Button>
      </div>

      <Row className="justify-content-md-center">
        <Col xs={12} className="mb-4 d-none d-sm-block">
          <SalesValueWidget
            title="Net Value"
            value={netWorth}
            percentage={10.57}
          />
        </Col>
        <Col xs={12} className="mb-4 d-sm-none">
          <SalesValueWidgetPhone
            title="Net Value"
            value={netWorth}
            percentage={10.57}
          />
        </Col>
        <Col xs={12} sm={6} xl={4} className="mb-4">
          <CounterWidget
            category="Weekly Tickets"
            title="345k"
            period="Feb 1 - Apr 1"
            percentage={18.2}
            icon={faChartLine}
            iconColor="shape-secondary"
          />
        </Col>

        <Col xs={12} sm={6} xl={4} className="mb-4">
          <CounterWidget
            category="Revenue"
            title="$43,594"
            period="Feb 1 - Apr 1"
            percentage={28.4}
            icon={faCashRegister}
            iconColor="shape-tertiary"
          />
        </Col>

        <Col xs={12} sm={6} xl={4} className="mb-4">
          <CircleChartWidget
            title="Traffic Share"
            data={trafficShares} />
        </Col>
      </Row>

      <Row>
        <Col xs={12} xl={12} className="mb-4">
          <Row>
            <Col xs={12} xl={8} className="mb-4">
              <Row>
                {/* <Col xs={12} className="mb-4">
                  <PageVisitsTable />
                </Col> */}

                <Col xs={12} lg={6} className="mb-4">
                  <TeamMembersWidget />
                </Col>

                <Col xs={12} lg={6} className="mb-4">
                  <ProgressTrackWidget />
                </Col>
              </Row>
            </Col>
            <Col xs={12} xl={4}>
              <Row>
                <Col xs={12} className="px-0">
                  <AcquisitionWidget />
                </Col>
              </Row>
            </Col>
          </Row>
        </Col>
      </Row>
    </>
  );
};
