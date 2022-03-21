"""
按时间段、站号检索地面数据要素

getSurfEleByTimeRangeAndStaID
"""

import pandas as pd

from nuwe_cmadaas.obs import retrieve_obs_station


def test_hourly(start_date, end_date, start_station_id, end_station_id):
    table = retrieve_obs_station(
        "SURF_CHN_MUL_HOR",
        time=pd.Interval(
            start_date, end_date,
            closed="left",
        ),
        station=[start_station_id, end_station_id]
    )
    print(table)


def test_hourly_station_id(start_date, end_date, station_id):
    table = retrieve_obs_station(
        "SURF_CHN_MUL_HOR",
        time=[start_date, end_date],
        station=station_id,
    )
    print(table)
