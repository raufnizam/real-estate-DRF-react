import { useState } from "react";

const SearchBar = ({ onSearch }) => {
    const [searchInputs, setSearchInputs] = useState({ country: "", address: "" });
  
    const handleInputChange = (e) => {
      setSearchInputs({ ...searchInputs, [e.target.name]: e.target.value });
    };
  
    const handleSearch = () => {
      onSearch(searchInputs);
    };
  
    return (
      <div className="mb-4">
        <input
          type="text"
          name="country"
          placeholder="Search by Country"
          value={searchInputs.country}
          onChange={handleInputChange}
          className="border p-2 mr-2 rounded"
        />
        <input
          type="text"
          name="address"
          placeholder="Search by Address"
          value={searchInputs.address}
          onChange={handleInputChange}
          className="border p-2 mr-2 rounded"
        />
        <button
          onClick={handleSearch}
          className="bg-blue-500 text-white p-2 rounded ml-2 hover:bg-blue-600"
        >
          Search
        </button>
      </div>
    );
  };
  
  export default SearchBar;
  