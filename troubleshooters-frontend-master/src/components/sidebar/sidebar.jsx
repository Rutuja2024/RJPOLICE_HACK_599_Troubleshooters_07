import "./sidebar.jsx";
import { MdDashboard } from "react-icons/md";
import { IoMdNotifications } from "react-icons/io";
import { MdTipsAndUpdates } from "react-icons/md";
import { FaSignOutAlt } from "react-icons/fa";
import { Link } from "react-router-dom";
const Sidebar = () => {
  return (
    <div className="side-bar pb-11 pr-10">
      <div>
        <div className="mb-8">
          <img
            className="logo mx-auto h-10 w-auto mt-8 ml-8 mb-5"
            src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600"
            alt="Your Company"
          />
        </div>
        <div className="mt-5">
          <Link
            to={"/dashboard"}
            className="items ml-5 gap-2 mb-3 hover:bg-indigo-600 py-2 px-4 rounded-lg hover:text-white"
          >
            <MdDashboard className="text-3xl text-white hover:text-white" />
            <h3 className="text-lg text-white">Dashboard</h3>
          </Link>
          <Link
            to={"/dashboard/notifications"}
            className="items ml-5 gap-2 mb-3 hover:bg-indigo-600 py-2 px-4 rounded-lg hover:text-white"
          >
            <IoMdNotifications className="text-3xl text-white hover:text-white" />
            <h3 className="text-lg text-white">Notifications</h3>
          </Link>
          <Link
            to={"/dashboard/opencases"}
            className="items ml-5 gap-2 mb-3 hover:bg-indigo-600 py-2 px-4 rounded-lg hover:text-white"
          >
            <MdTipsAndUpdates className="text-3xl text-white hover:text-white" />
            <h3 className="text-lg text-white">Open Cases</h3>
          </Link>
        </div>
      </div>
      <Link
        to={"/"}
        className="logout flex ml-5 gap-2 py-2 px-6 rounded-lg bg-indigo-600 hover:bg-indigo-400"
      >
        <FaSignOutAlt className="text-2xl text-white" />
        <button className="text-lg text-white">Sign out</button>
      </Link>
    </div>
  );
};

export default Sidebar;
