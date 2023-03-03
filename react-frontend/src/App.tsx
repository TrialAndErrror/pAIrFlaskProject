import reactLogo from './assets/react.svg'
import TemperatureScreen from "./components/TemperaturePage/Screen";
import FeedingCalcScreen from "./components/FeedingCalcPage/Screen";
import "./index.less"
import {useState} from "react";
import {Container, Footer, Header} from "rsuite";
import NavMenu from "./components/Navbar/Navbar";
import EntriesChart from "./components/TemperaturePage/EntriesChart";
import {useMediaQuery} from "react-responsive";

function App() {
    const [currentPage, setCurrentPage] = useState('temperature')

    const isTabletOrMobile = useMediaQuery({query: '(max-width: 1224px)'})
    console.log(import.meta.env.VITE_API_URL)

    return (
        <div className="bg rs-theme-dark">
            <NavMenu active={currentPage} setActive={setCurrentPage}/>
            <Container>
                {currentPage === "temperature" && <TemperatureScreen smallSize={isTabletOrMobile}/>}
                {currentPage === "calc" && <FeedingCalcScreen smallSize={isTabletOrMobile}/>}

            </Container>
            <Container>
                <Footer><br/></Footer>
            </Container>
        </div>
    );
}

export default App
