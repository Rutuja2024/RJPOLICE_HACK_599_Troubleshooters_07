import "./dashboard.css";
import { CiSearch } from "react-icons/ci";
import { CiBank } from "react-icons/ci";
import Notification from "../../components/notifications/notification";
import { IoDownloadOutline } from "react-icons/io5";
import { MdOutlineSecurity } from "react-icons/md";
import Sidebar from "../../components/sidebar/sidebar";
import { IoIosNotificationsOutline } from "react-icons/io";
import { useNavigate } from "react-router-dom";
import * as React from "react";
import { DemoContainer } from "@mui/x-date-pickers/internals/demo";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import { DatePicker } from "@mui/x-date-pickers/DatePicker";

const Dashboard = () => {
  const navigate = useNavigate();

  const handleAccountClick = () => {
    navigate("/dashboard/account/:id");
  };
  return (
    <>
      <div className="main-div flex justify-between gap-1">
        <div className='w-96'>
          <Sidebar />
        </div>
        <div className="middle-div">
          <div className=" px-3 py-5 pl-5">
            <div className="flex justify-between mb-5">
              <div className="stats border rounded-lg border-indigo-600 py-8 px-14 ">
                <h1 className="text-4xl font-bold text-indigo-600">900+</h1>
                <p className="text-lg">Solved Cases</p>
              </div>
              <div className="stats border rounded-lg border-indigo-600 py-8 px-16 mx-2">
                <h1 className="text-4xl font-bold text-indigo-600">600+</h1>
                <p className="text-lg">Open Cases</p>
              </div>
              <div className="stats border rounded-lg border-indigo-600 py-8 px-14">
                <h1 className="text-4xl font-bold text-indigo-600">300+</h1>
                <p className="text-lg">Fraud Accounts</p>
              </div>
            </div>
            <div className="accounts px-8 py-8">
              <div>
                <h1 className="text-3xl font-bold mb-5 text-indigo-600">
                  Accounts Listed
                </h1>
              </div>
              <div className="flex items-center">
                <input
                  id="search"
                  name="search"
                  type="text"
                  placeholder="Search "
                  className="py-1 px-5 border-solid border-y border-l rounded-l-md w-full"
                />
                <div className=" px-2 py-2 border-solid border-y border-r rounded-r-md">
                  <CiSearch className="" />
                </div>
                <div className="ml-4 border py-1 px-5 pr-8 rounded-md bg-indigo-600">
                  <select
                    name="filter"
                    id="filter"
                    className="bg-indigo-600 text-white"
                  >
                    <option value="Filter1">Filter1</option>
                    <option value="filter2">filter2</option>
                  </select>
                </div>
              </div>
              <div className="accounts-listed mt-8">
                <div
                  onClick={handleAccountClick}
                  className="flex items-center border-solid border rounded px-5 py-3 my-2"
                >
                  <div className="text-3xl bg-indigo-600 text-white rounded-full p-1">
                    <CiBank />
                  </div>
                  <div className="ml-5">
                    <h2 className="font-bold text-lg">Vishal Borse</h2>
                    <h2 className="text-gray-500">
                      Account Number : 12458693254
                    </h2>
                  </div>
                </div>
                <div
                  onClick={handleAccountClick}
                  className="flex items-center border-solid border rounded px-5 py-3 my-2"
                >
                  <div className="text-3xl bg-indigo-600 text-white rounded-full p-1">
                    <CiBank />
                  </div>
                  <div className="ml-5">
                    <h2 className="font-bold text-lg">Vishal Borse</h2>
                    <h2 className="text-gray-500">
                      Account Number : 12458693254
                    </h2>
                  </div>
                </div>
                <div
                  onClick={handleAccountClick}
                  className="flex items-center border-solid border rounded px-5 py-3 my-2"
                >
                  <div className="text-3xl bg-indigo-600 text-white rounded-full p-1">
                    <CiBank />
                  </div>
                  <div className="ml-5">
                    <h2 className="font-bold text-lg">Vishal Borse</h2>
                    <h2 className="text-gray-500">
                      Account Number : 12458693254
                    </h2>
                  </div>
                </div>
                <div
                  onClick={handleAccountClick}
                  className="flex items-center border-solid border rounded px-5 py-3 my-2"
                >
                  <div className="text-3xl bg-indigo-600 text-white rounded-full p-1">
                    <CiBank />
                  </div>
                  <div className="ml-5">
                    <h2 className="font-bold text-lg">Vishal Borse</h2>
                    <h2 className="text-gray-500">
                      Account Number : 12458693254
                    </h2>
                  </div>
                </div>
                <div
                  onClick={handleAccountClick}
                  className="flex items-center border-solid border rounded px-5 py-3 my-2"
                >
                  <div className="text-3xl bg-indigo-600 text-white rounded-full p-1">
                    <CiBank />
                  </div>
                  <div className="ml-5">
                    <h2 className="font-bold text-lg">Vishal Borse</h2>
                    <h2 className="text-gray-500">
                      Account Number : 12458693254
                    </h2>
                  </div>
                </div>
                <div
                  onClick={handleAccountClick}
                  className="flex items-center border-solid border rounded px-5 py-3 my-2"
                >
                  <div className="text-3xl bg-indigo-600 text-white rounded-full p-1">
                    <CiBank />
                  </div>
                  <div className="ml-5">
                    <h2 className="font-bold text-lg">Vishal Borse</h2>
                    <h2 className="text-gray-500">
                      Account Number : 12458693254
                    </h2>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="right-div p-5 pl-3">
          <div className="noti p-5">
            <div>
              <h1 className="text-3xl font-bold mb-5 text-indigo-600">
                Notifications
              </h1>
            </div>
            <div className="noti-list">
              <div className="flex gap-3 items-center border-solid border rounded my-2 ">
                <div className=" flex border border-indigo-600 items-centre py-1 px-2 text-2xl rounded-full ml-2">
                  <IoIosNotificationsOutline />
                </div>
                <div className="">
                  <h2 className="text-gray-600 py-1">
                    {" "}
                    Unusual activity detected: A transaction of $X has been made
                    in Jaipur, Rajasthan.
                  </h2>
                </div>
              </div>
              <div className="flex gap-3 items-center border-solid border rounded my-2">
                <div className=" flex border border-indigo-600 items-centre py-1 px-2 text-2xl rounded-full ml-2">
                  <IoIosNotificationsOutline />
                </div>
                <div className="">
                  <h2 className="text-gray-600 py-1">
                    {" "}
                    Unusual activity detected: A transaction of $X has been made
                    in Jaipur, Rajasthan.
                  </h2>
                </div>
              </div>
              <div className="flex gap-3 items-center border-solid border rounded my-2">
                <div className=" flex border border-indigo-600 items-centre py-1 px-2 text-2xl rounded-full ml-2">
                  <IoIosNotificationsOutline />
                </div>
                <div className="">
                  <h2 className="text-gray-600 py-1">
                    {" "}
                    Unusual activity detected: A transaction of $X has been made
                    in Jaipur, Rajasthan.
                  </h2>
                </div>
              </div>
              <div className="flex gap-3 items-center border-solid border rounded my-2">
                <div className=" flex border border-indigo-600 items-centre py-1 px-2 text-2xl rounded-full ml-2">
                  <IoIosNotificationsOutline />
                </div>
                <div className="">
                  <h2 className="text-gray-600 py-1">
                    {" "}
                    Unusual activity detected: A transaction of $X has been made
                    in Jaipur, Rajasthan.
                  </h2>
                </div>
              </div>
              <div className="flex gap-3 items-center border-solid border rounded my-2">
                <div className=" flex border border-indigo-600 items-centre py-1 px-2 text-2xl rounded-full ml-2">
                  <IoIosNotificationsOutline />
                </div>
                <div className="">
                  <h2 className="text-gray-600 py-1">
                    {" "}
                    Unusual activity detected: A transaction of $X has been made
                    in Jaipur, Rajasthan.
                  </h2>
                </div>
              </div>
              <div className="flex gap-3 items-center border-solid border rounded my-2">
                <div className=" flex border border-indigo-600 items-centre py-1 px-2 text-2xl rounded-full ml-2">
                  <IoIosNotificationsOutline />
                </div>
                <div className="">
                  <h2 className="text-gray-600 py-1">
                    {" "}
                    Unusual activity detected: A transaction of $X has been made
                    in Jaipur, Rajasthan.
                  </h2>
                </div>
              </div>
              <div className="flex gap-3 items-center border-solid border rounded my-2">
                <div className=" flex border border-indigo-600 items-centre py-1 px-2 text-2xl rounded-full ml-2">
                  <IoIosNotificationsOutline />
                </div>
                <div className="">
                  <h2 className="text-gray-600 py-1">
                    {" "}
                    Unusual activity detected: A transaction of $X has been made
                    in Jaipur, Rajasthan.
                  </h2>
                </div>
              </div>
              <div className="flex gap-3 items-center border-solid border rounded my-2">
                <div className=" flex border border-indigo-600 items-centre py-1 px-2 text-2xl rounded-full ml-2">
                  <IoIosNotificationsOutline />
                </div>
                <div className="">
                  <h2 className="text-gray-600 py-1">
                    {" "}
                    Unusual activity detected: A transaction of $X has been made
                    in Jaipur, Rajasthan.
                  </h2>
                </div>
              </div>
            </div>
          </div>
          <div className="lower mt-6  flex items-center justify-between gap-5">
            <div className="report p-8">
              <div className="text-2xl font-bold text-indigo-600 mb-1">
                <h1>Download Reports</h1>
              </div>
              <div className="flex items-center">
                <div className="">
                  <LocalizationProvider dateAdapter={AdapterDayjs}>
                    <DemoContainer
                      components={["DatePicker", "DatePicker", "DatePicker"]}
                    >
                      <DatePicker
                        label={'"month" and "year"'}
                        views={["month", "year"]}
                      />
                    </DemoContainer>
                  </LocalizationProvider>
                </div>
                <div className=" ml-2 rounded bg-indigo-600 text-white px-3 py-4 mt-2">
                  <IoDownloadOutline className="text-2xl" />
                </div>
              </div>
            </div>
            <div className="flex-column items-center justify-center bg-indigo-600 pl-8 py-10 rounded-lg text-white">
              <div>
                <MdOutlineSecurity className="text-3xl" />
              </div>
              <div>
                {" "}
                <h1 className="text-lg">Report Fraud</h1>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};
export default Dashboard;
