import reactLogo from './assets/react.svg'
import TemperatureScreen from "./components/TemperaturePage/Screen";
import "./index.less"
import {useState} from "react";
import {Container, Footer, Header} from "rsuite";
import NavMenu from "./components/Navbar/Navbar";
import EntriesChart from "./components/TemperaturePage/EntriesChart";

function App() {
    const [currentPage, setCurrentPage] = useState('temperature')


    return (
        <div className="bg rs-theme-dark">
            <NavMenu/>
            <Container>
                {currentPage === "temperature" && <TemperatureScreen/>}
            </Container>
            <Container>
                <Footer><br /></Footer>
            </Container>
        </div>
    );
}

export default App
