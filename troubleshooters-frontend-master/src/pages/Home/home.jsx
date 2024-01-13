import { Link } from "react-router-dom";
const Home = () => {
  return (
    <>
      <div className="flex-column items-center m-10">
        <div>
          <h1 className="text-3xl font-bold text-centre">
            {" "}
            Rajasthan Police Hackathon
          </h1>
        </div>
        <div>
          <Link to={"/adminlogin"} className="text-white bg-indigo-600 p-10 m-5">
            Admin Login
          </Link>
          <Link to={"/"} className="text-white bg-indigo-600 p-10 m-5">
            User Login
          </Link>
        </div>
      </div>
    </>
  );
};
export default Home;
