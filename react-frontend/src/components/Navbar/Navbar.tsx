import { Navbar, Nav } from 'rsuite';
import HomeIcon from '@rsuite/icons/legacy/Home';
import CogIcon from '@rsuite/icons/legacy/Cog';

const NavMenu = () => (
  <Navbar>
    <Navbar.Brand href="#">Devbox</Navbar.Brand>
    <Nav>
      <Nav.Item>Temperature</Nav.Item>

    </Nav>
    <Nav pullRight>
      <Nav.Item icon={<CogIcon />}>Settings</Nav.Item>
    </Nav>
  </Navbar>
);


export {NavMenu as default}
