import { useEffect, useState } from "react";

const Properties = () => {
  const [properties, setProperties] = useState([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState("");
  const [availability, setAvailability] = useState("");
  const [tag, setTag] = useState("");

  const fetchProperties = async (params = {}) => {
    setLoading(true);
    try {
      // Construct query parameters
      const queryParams = new URLSearchParams(params);
      const response = await fetch(`http://127.0.0.1:8002/api/properties/?${queryParams.toString()}`);
      if (response.ok) {
        const data = await response.json();
        setProperties(data);
      } else {
        console.error("Failed to fetch properties");
      }
    } catch (error) {
      console.error("Error:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = (e) => {
    e.preventDefault(); // Prevent form submission from refreshing the page
    const params = {};
    if (search) params.search = search;
    if (availability) params.availability = availability;
    if (tag) params.tag = tag;
    fetchProperties(params);
  };

  useEffect(() => {
    // Fetch all properties when the page loads
    fetchProperties();
  }, []);

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Properties</h1>

      {/* Search Form */}
      <form onSubmit={handleSearch} className="mb-4 flex flex-wrap gap-4">
        <input
          type="text"
          placeholder="Search by country or address"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="border p-2 rounded"
        />
        <input
          type="text"
          placeholder="Filter by availability"
          value={availability}
          onChange={(e) => setAvailability(e.target.value)}
          className="border p-2 rounded"
        />
        <input
          type="text"
          placeholder="Filter by tag"
          value={tag}
          onChange={(e) => setTag(e.target.value)}
          className="border p-2 rounded"
        />
        <button
          type="submit"
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          Search
        </button>
      </form>

      {loading ? (
        <div>Loading...</div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {properties.length > 0 ? (
            properties.map((property) => (
              <div
                key={property.id}
                className="border p-4 rounded shadow hover:shadow-lg transition-shadow"
              >
                <h2 className="text-xl font-semibold">{property.title}</h2>
                <p>{property.address}</p>
                <p>{property.country}</p>
                <p>Price: ${property.price}</p>
                <p>Availability: {property.availability}</p>
              </div>
            ))
          ) : (
            <div>No properties found.</div>
          )}
        </div>
      )}
    </div>
  );
};

export default Properties;
