import EntriesTable from "./EntriesTable";
import {Container, Content, Panel} from "rsuite";
import EntriesChart from "./EntriesChart";
import useFetch from "react-fetch-hook";
import {DataType} from "./types";

const TemperatureScreen = () => {
    const endpoint = "http://localhost:56000/data"
    const {data: fetchedData, isLoading} = useFetch(endpoint)

    if (isLoading) return <Panel header="Loading Temperature Data" bordered className="card-wide bg-light"/>

    const data = fetchedData as DataType[]
    if (data.length === 0) {
        return (
            <Container>
                <div className="container">
                    <Panel header="No Temperature Data Found!" bordered className="card-wide bg-light">
                        Please wait for data to appear in the database.
                    </Panel>
                </div>
            </Container>
        )
    }

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