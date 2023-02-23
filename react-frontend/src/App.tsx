import TemperatureScreen from "./components/TemperaturePage/Screen";
import "./index.less"
import { useState } from "react";
import { Container, Footer } from "rsuite";
import NavMenu from "./components/Navbar/Navbar";
import { useMediaQuery } from "react-responsive";

function App() {
    const [currentPage, setCurrentPage] = useState('temperature')

    const isMobileSize = useMediaQuery({ query: '(max-width: 1224px)' })

    const temperatureEndpoint = import.meta.env.VITE_TEMPERATURE_ENDPOINT

    console.log(temperatureEndpoint)
    const temperatureProps = {
        mobileScreenSize: isMobileSize,
        temperatureEndpoint
    }

    return (
        <div className="bg rs-theme-dark">
            <NavMenu />
            <Container>
                {currentPage === "temperature" && <TemperatureScreen {...temperatureProps} />}
            </Container>
            <Container>
                <Footer><br /></Footer>
            </Container>
        </div>
    );
}

export default App
