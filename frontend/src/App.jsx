import { useState } from "react";
import { searchAddress } from "./api/opensearch";
import "./App.css";
import { Autocomplete, TextField } from "@mui/material";

function App() {
  const [results, setResults] = useState([]);

  const handleSearch = async (event) => {
    event.preventDefault();
    const results = await searchAddress(event.target.value);
    setResults(results);
  };

  return (
    <>
      <h1>Address search</h1>
      <Autocomplete
        onInputChange={handleSearch}
        options={results.map((result) => {
          return `${result._source.street} ${result._source.house_number}, ${result._source.postal_code}, ${result._source.municipality}`;
        })}
        renderInput={(params) => (
          <TextField
            {...params}
            sx={{
              "& .MuiInputBase-input": { color: "white" },
              "& .MuiOutlinedInput-root .MuiOutlinedInput-notchedOutline": {
                borderColor: "white",
              },
              "& .MuiAutocomplete-clearIndicator": { color: "white" },
              "& .MuiAutocomplete-popupIndicator": { color: "white" },
            }}
          />
        )}
      />
    </>
  );
}

export default App;
