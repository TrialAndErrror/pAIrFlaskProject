import {useState} from "react";
import {
    DomainTuple,
    VictoryAxis,
    VictoryBrushContainer,
    VictoryChart,
    VictoryLine,
    VictoryZoomContainer
} from "victory";
import {Panel} from "rsuite";
import useFetch from "react-fetch-hook";
import {DataType, FormattedDataType} from "./types";

type ZoomDomainObject = {
    x?: DomainTuple
    y?: DomainTuple
}

type EntriesChartProps = {
    data: FormattedDataType[],
}

const EntriesChart = ({data}: EntriesChartProps) => {
    const [zoomDomain, setZoomDomain] = useState({} as ZoomDomainObject)

    return (
        <Panel header="Temperature Data" bordered className="card-wide bg-light">
            <VictoryChart
                width={600}
                height={270}
                scale={{x: "time"}}
                containerComponent={
                    <VictoryZoomContainer
                        zoomDimension="x"
                        zoomDomain={zoomDomain}
                        onZoomDomainChange={(domain) => setZoomDomain((domain))}
                    />
                }
            >
                <VictoryLine
                    interpolation={'basis'}
                    label={"Temperature"}
                    style={{
                        data: {stroke: "orange"}
                    }}
                    data={data}
                    x="created_at"
                    y="temperature"
                />
                <VictoryLine
                    interpolation={'basis'}
                    label={"Humidity"}
                    style={{
                        data: {stroke: "blue"}
                    }}
                    data={data}
                    x="created_at"
                    y="humidity"
                />

            </VictoryChart>
            <VictoryChart
                padding={{top: 0, left: 50, right: 50, bottom: 30}}
                width={600} height={100} scale={{x: "time"}}
                containerComponent={
                    <VictoryBrushContainer
                        brushDimension="x"
                        brushDomain={zoomDomain}
                        onBrushDomainChange={(domain) => setZoomDomain(domain)}
                    />
                }
            >
                <VictoryAxis
                    tickFormat={(x) => new Date(x).getFullYear()}
                />
                <VictoryLine
                    interpolation={'basis'}
                    label={"Temperature"}
                    style={{
                        data: {stroke: "red"}
                    }}
                    data={data}
                    x="created_at"
                    y="temperature"
                />
                <VictoryLine
                    interpolation={'basis'}
                    label={"Humidity"}
                    style={{
                        data: {stroke: "blue"}
                    }}
                    data={data}
                    x="created_at"
                    y="humidity"
                />
            </VictoryChart>
        </Panel>
    )
}

export {EntriesChart as default}