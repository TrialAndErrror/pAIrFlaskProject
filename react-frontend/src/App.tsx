import reactLogo from './assets/react.svg'
import TemperatureScreen from "./components/TemperaturePage/Screen";
import "./index.less"
import {useState} from "react";
import {Container, Footer, Header} from "rsuite";
import NavMenu from "./components/Navbar/Navbar";
import EntriesChart from "./components/TemperaturePage/EntriesChart";
import {useMediaQuery} from "react-responsive";

function App() {
    const [currentPage, setCurrentPage] = useState('temperature')

    const isTabletOrMobile = useMediaQuery({ query: '(max-width: 1224px)' })

    return (
        <div className="bg rs-theme-dark">
            <NavMenu/>
            <Container>
                {currentPage === "temperature" && <TemperatureScreen smallSize={isTabletOrMobile}/>}
            </Container>
            <Container>
                <Footer><br /></Footer>
            </Container>
        </div>
    );
}

export default App
