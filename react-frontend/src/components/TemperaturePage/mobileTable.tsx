import {Panel, Table} from "rsuite";
import {FormattedDataType} from "./types";


const MobileTable = ({data}: {data: FormattedDataType[]}) => {

    if (data.length === 0) {
        return <p>No Data available!</p>
    }

    const sortedData = data.sort((a, b) => b.created_at.getTime() - a.created_at.getTime());

    return (
        <>
            <Panel header="Temperature Data" bordered className="card-wide bg-dark">
                <Table virtualized data={data} bordered={true}>
                    <Table.Column flexGrow={1} align="center" fixed>
                        <Table.HeaderCell>Time</Table.HeaderCell>
                        <Table.Cell dataKey="created_at_mobile"/>
                    </Table.Column>

                    <Table.Column flexGrow={1}>
                        <Table.HeaderCell>Temperature</Table.HeaderCell>
                        <Table.Cell dataKey="temperature"/>
                    </Table.Column>

                    <Table.Column flexGrow={1}>
                        <Table.HeaderCell>Humidity</Table.HeaderCell>
                        <Table.Cell dataKey="humidity"/>
                    </Table.Column>
                </Table>
            </Panel>
        </>
    )
}

const EntriesTableCard = () => {

}

export {MobileTable as default}