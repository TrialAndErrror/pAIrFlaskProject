import EntriesTable from "./EntriesTable";
import {Container, Content, Panel} from "rsuite";
import EntriesChart from "./EntriesChart";
import useFetch from "react-fetch-hook";
import {DataType} from "./types";

const TemperatureScreen = () => {
    const {data: fetchedData, isLoading} = useFetch("http://localhost:80/data")

    if (isLoading) return <Panel header="Loading Temperature Data" bordered className="card-wide bg-light" />

    const data = fetchedData as DataType[]

    return (
        <>
            <Container>
                <div className="container">
                    <EntriesChart data={data}/>
                </div>
            </Container>
            <Container>
                <div className="container">
                    <EntriesTable data={data}/>
                </div>
            </Container>
        </>
    )
}

export {TemperatureScreen as default}