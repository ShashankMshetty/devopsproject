import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

function MovieDetail({ movie }) {
  const [details, setDetails] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    if (!movie) {
      return;
    }

    axios
      .get(`${process.env.REACT_APP_MOVIE_API_URL}/movies/${movie.id}`)
      .then((response) => {
        setDetails(response.data);
        setError('');
      })
      .catch(() => {
        setError('Unable to load movie details. Please try again later.');
      });
  }, [movie]);

  return (
    <div>
      {error && <p role="alert">{error}</p>}
      <h2>{details?.movie?.title}</h2>
      <p>{details?.movie?.description}</p>
    </div>
  );
}

MovieDetail.propTypes = {
  movie: PropTypes.shape({
    id: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
  }),
};

export default MovieDetail;
