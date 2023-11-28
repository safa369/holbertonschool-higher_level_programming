-- max temperature.
SELECT state, max(value) as max_temp
from temperatures
GROUP BY state
ORDER BY state;