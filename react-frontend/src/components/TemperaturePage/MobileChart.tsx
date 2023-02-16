import {useState} from "react";
import {
    DomainTuple,
    VictoryAxis,
    VictoryBrushContainer,
    VictoryChart, VictoryContainer,
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

const MobileChart = ({data}: EntriesChartProps) => {
    const limitedData = data.slice(0, 360) // Limit to 6 hours of data (720 minutes)
    return (
        <>
            <div className="container-mobile">

                <Panel header="Temperature" bordered className="card-wide bg-light">
                    <VictoryChart
                        scale={{x: "time"}}
                        height={500}
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

                    </VictoryChart>
                </Panel>
            </div>
            <div className="container-mobile">

                <Panel header="Humidity" bordered className="card-wide bg-light">

                    <VictoryChart
                        scale={{x: "time"}}
                        height={500}
                    >
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
            </div>
        </>
    )
}

export {MobileChart as default}