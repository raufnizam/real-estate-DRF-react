import { useEffect, useState } from "react";

const Properties = () => {
  const [properties, setProperties] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProperties = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8002/api/properties/");
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

    fetchProperties();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Properties</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {properties.map((property) => (
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
        ))}
      </div>
    </div>
  );
};

export default Properties;
