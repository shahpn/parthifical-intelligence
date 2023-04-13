import React  from 'react';
import { Container, Row, Col } from "react-bootstrap";

const Footer = () => {
    return (
      <footer className="footer">
        <Container>
          <Row className="align-items-center">
            {/* <MailchimpForm /> */}
            <Col size={12} sm={6}>
              {/* <img src={logo} alt="Logo" /> */}
            </Col>
            <Col size={12} sm={6} className="text-center text-sm-end">
              {/* <div className="social-icon"> */}
                {/* eslint-disable-next-line */}
                {/* <a target="_blank" href="https://www.linkedin.com/in/gabriel-nulman/"><img src={navIcon1} alt="Icon" width={'16px'} height={'16px'}/></a> */}
                {/* <a href="#"><img src={navIcon2} alt="Icon" /></a>
                <a href="#"><img src={navIcon3} alt="Icon" /></a> */}
                {/* eslint-disable-next-line */}  
                {/* <a target="_blank" href="https://github.com/YoYoGavri"><img src={github} alt="" width={'30px'} height={'30px'}/></a> */}
              {/* </div> */}
              <p>Copyright 2023. All Rights Reserved</p>
            </Col>
          </Row>
        </Container>
      </footer>
    );
  }

  export default Footer;