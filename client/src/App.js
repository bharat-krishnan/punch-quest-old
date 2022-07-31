import React, {useRef} from 'react'
import './style.css'
import { Container, Row, Col, Button, Icon, Navbar, NavItem } from 'react-materialize';
import gloves from './assets/images/redGloves.png'
// import idealGloves from './assets/images/idealGloves.png'
import Texture from './components/Texture'
import 'materialize-css';

const App = () => {
  const myRef = useRef(null)

  const executeScroll = () => myRef.current.scrollIntoView({ behavior: 'smooth' })   

  return (
    <div>
      <Container>
        <Row/>
        <Navbar className="customNav red z-depth-0 lighten-1"
          alignLinks="right"
          brand={<a className="brand-logo" href="#"></a>}
          id="mobile-nav"
          menuIcon={<Icon>menu</Icon>}
          options={{
            draggable: true,
            edge: 'left',
            inDuration: 250,
            onCloseEnd: null,
            onCloseStart: null,
            onOpenEnd: null,
            onOpenStart: null,
            outDuration: 200,
            preventScrolling: true
          }}
        >
          <NavItem className = "customNavItem" href="">
            about
          </NavItem>
          <NavItem className = "customNavItem" href="">
            demo 
          </NavItem>
          <NavItem className = "customNavItem" href="">
            login
          </NavItem>
        </Navbar>

        <Row className="above" />
        <Row className="center-align">
        <h1 className="title">COMBAT.AI</h1>

          <Button onClick={executeScroll} className="subtitleButton z-depth-0">Pick up the gloves</Button>
          {/* <h5 className = "subtitle">Pick up the gloves</h5> */}

        </Row>
        <Row>
        <a onClick={executeScroll}>
            <img className="floating" width="128" src={gloves} alt="gloves" />
        </a>
        </Row>
      </Container>

      <Texture/>
      <div ref = {myRef}></div>
          
    </div>
  )
}

export default App