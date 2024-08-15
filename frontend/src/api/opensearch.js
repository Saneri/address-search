import axios from "axios";

export const searchAddress = async (query) => {
  const response = await axios.post(
    "/api/addresses/_search",
    {
      query: {
        match_phrase_prefix: {
          street: query,
        },
      },
      size: 10000,
    },
    {
      headers: {
        // took this straight from Postman because had problems
        Authorization: `Basic YWRtaW46J1JRNDMtM0ptJjQqX0RcaTEzc0phYi0ydzMzSTl7SGI=`,
      },
    }
  );

  return response.data.hits.hits;
};
