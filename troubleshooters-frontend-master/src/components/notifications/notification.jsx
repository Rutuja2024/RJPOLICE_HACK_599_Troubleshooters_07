import "./notification.css";
import { IoIosNotificationsOutline } from "react-icons/io";

const Notification = () => {
  return (
    <>
      <div className="notifications">
        <div>
          <h1 className="text-3xl font-bold mb-5 text-indigo-600">
            Notifications
          </h1>
        </div>
        <div className="noti-lists mt-8">
          <div className="flex items-center border-solid border rounded px-5 py-3 my-2">
            <div className="text-xl text-indigo-600 border-indigo-600 border rounded-full p-1">
              <IoIosNotificationsOutline />
            </div>
            <div className="ml-2">
              <h2 className="text-gray-600">
                {" "}
                Unusual activity detected: A transaction of $X has been made in
                Jaipur, Rajasthan.
              </h2>
            </div>
          </div>
          <div className="flex items-center border-solid border rounded px-5 py-3 my-2">
            <div className="text-xl text-indigo-600 border-indigo-600 border rounded-full p-1">
              <IoIosNotificationsOutline />
            </div>
            <div className="ml-2">
              <h2 className="text-gray-600">
                {" "}
                A large transaction of $X has been made.
              </h2>
            </div>
          </div>
          <div className="flex items-center border-solid border rounded px-5 py-3 my-2">
            <div className="text-xl text-indigo-600 border-indigo-600 border rounded-full p-1">
              <IoIosNotificationsOutline />
            </div>
            <div className="ml-2">
              <h2 className="text-gray-600">
                {" "}
                A large transaction of $X has been made.
              </h2>
            </div>
          </div>
          <div className="flex items-center border-solid border rounded px-5 py-3 my-2">
            <div className="text-xl text-indigo-600 border-indigo-600 border rounded-full p-1">
              <IoIosNotificationsOutline />
            </div>
            <div className="ml-2">
              <h2 className="text-gray-600">
                {" "}
                Unusual payment pattern detected
              </h2>
            </div>
          </div>
          <div className="flex items-center border-solid border rounded px-5 py-3 my-2">
            <div className="text-xl text-indigo-600 border-indigo-600 border rounded-full p-1">
              <IoIosNotificationsOutline />
            </div>
            <div className="ml-2">
              <h2 className="text-gray-600"> Fraud Detection Success</h2>
            </div>
          </div>
          <div className="flex items-center border-solid border rounded px-5 py-3 my-2">
            <div className="text-xl text-indigo-600 border-indigo-600 border rounded-full p-1">
              <IoIosNotificationsOutline />
            </div>
            <div className="ml-2">
              <h2 className="text-gray-600"> Bank Account Details Available</h2>
            </div>
          </div>
          <div className="flex items-center border-solid border rounded px-5 py-3 my-2">
            <div className="text-xl text-indigo-600 border-indigo-600 border rounded-full p-1">
              <IoIosNotificationsOutline />
            </div>
            <div className="ml-2">
              <h2 className="text-gray-600"> Possible Fake Account Detected</h2>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};
export default Notification;
