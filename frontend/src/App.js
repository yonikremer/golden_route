import React, { useState } from "react";
import { BrowserRouter as Router } from "react-router-dom";
import { Link } from "react-router-dom";
import Weather from "./Weather";
import Main from "./Main";

function NavBar() {
  const [currentPage, setCurrentPage] = useState("Weather");

  return (
      <Router>
          <div>
              <nav>
                  <Link to={`/${currentPage === "Weather" ? "Main" : "Weather"}`} onClick={() => setCurrentPage(currentPage === "Weather" ? "Main" : "Weather")}>
                      {currentPage === "Weather" ? "Main" : "Weather"}
                  </Link>
              </nav>
              {currentPage === "Weather" ? <Weather /> : <Main />}
          </div>
      </Router>
  );
}

export default NavBar;
