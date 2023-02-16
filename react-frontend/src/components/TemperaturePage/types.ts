import {Dayjs} from "dayjs";

export type DataType = {
    created_at: string,
    temperature: string,
    humidity: string
}

export type FormattedDataType = {
    created_at: Date,
    created_at_string: string
    temperature: string,
    humidity: string
}