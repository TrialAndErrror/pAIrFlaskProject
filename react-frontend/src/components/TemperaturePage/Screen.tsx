import EntriesTable from "./EntriesTable";
import {Container, Content, Panel} from "rsuite";
import EntriesChart from "./EntriesChart";
import useFetch from "react-fetch-hook";
import {DataType, FormattedDataType} from "./types";
import dayjs from "dayjs";

import utc from 'dayjs/plugin/utc';
import timezone from 'dayjs/plugin/timezone'
dayjs.extend(utc)
dayjs.extend(timezone)
dayjs.tz.setDefault("America/New_York")

const TemperatureScreen = () => {
    const endpoint = "http://192.168.1.183:55004/data"
    const {data, isLoading} = useFetch<DataType[]>(endpoint)

    if (isLoading) return <Panel header="Loading Temperature Data" bordered className="card-wide bg-light"/>

    if (!data || data.length === 0) {
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

    const formattedData: FormattedDataType[] = data.map((entry) => {
        const dateObject = dayjs(entry.created_at, {utc: true}).toDate()
        return {
            ...entry,
            created_at: dateObject,
            created_at_string: dateObject.toString()
        }
    })

    return (
        <>
            <Container>
                <div className="container">
                    <EntriesChart data={formattedData}/>
                </div>
            </Container>
            <Container>
                <div className="container">
                    <EntriesTable data={formattedData}/>
                </div>
            </Container>
        </>
    )
}

export {TemperatureScreen as default}