QUERY_MAP = {
    "Temperature": "SELECT time, value FROM \"CM_HAM_DO_AI1/Temp_value\" ORDER BY time DESC LIMIT 100",
    "pH": "SELECT time, value FROM \"CM_HAM_PH_AI1/pH_value\" ORDER BY time DESC LIMIT 100",
    "Oxygen": "SELECT time, value FROM \"CM_PRESSURE/Output\" ORDER BY time DESC LIMIT 100",
    "Pressure": "SELECT time, value FROM \"CM_PID_DO/Process_DO\" ORDER BY time DESC LIMIT 100"
}
