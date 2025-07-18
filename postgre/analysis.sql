-- What is the average temperature each month?
SELECT
	"Month",
	AVG("Temperature (C)") AS "avg_temprature"
FROM weather_data
GROUP BY Month
ORDER BY Month;
--In which months is the highest humidity recorded?
SELECT
	"Month",
	MAX("Humidity") AS "max_humidity"
FROM weather_data
GROUP BY MONTH
ORDER BY "max_humidity" DESC
LIMIT 5;
--How many days did it snow each year?
SELECT
	"Year",
	COUNT(*) AS snow_days,
FROM weather_data
WHERE "Precip Type" = "snow"
GROUP BY "Year"
ORDER BY "Year";
--Maximum and minimum air pressure by month
SELECT
	"Month",
	MAX("Pressure (millibars)") AS "max_pressure",
	MIN("Pressure (millibars)") AS "min_pressure"
FROM weather_data
GROUP BY "Month"
ORDER BY "Month";
--Number of days with humidity above the average for the month
SELECT
	COUNT(*) AS "number_of_days"
FROM weather_data
WHERE "Humidity" > "avg_Humidity";
--Periods when the average wind speed was more than 20km/h (monthly)
SELECT
	"Month",
	"Year",
	ROUND(AVG("Wind Speed (km/h)"), 2) AS avg_wind
FROM weather_data
GROUP BY "Year","Month"
HAVING AVG("Wind Speed (km/h)") > 20
ORDER BY "Year","Month";
--records by precipitation type
SELECT
  "Precip Type",
  COUNT(*) AS count
FROM weather_data
GROUP BY "Precip Type";
--Comparing the temperatures of the winter and summer months
SELECT
  CASE
    WHEN month IN (12, 1, 2) THEN 'Winter'
    WHEN month IN (6, 7, 8) THEN 'Summer'
    ELSE 'Other'
  END AS season,
  ROUND(AVG("Temperature (C)"), 2) AS avg_temp
FROM weather_data
GROUP BY season;