import Sidebar from "../../components/sidebar/sidebar";
import { IoIosNotificationsOutline } from "react-icons/io";
import { CiSearch } from "react-icons/ci";
import "./notification-page.css";
const NotificationPage = () => {
  return (
    <>
      <div className="flex item-centre">
        <div className="">
          <Sidebar className='w-96' />
        </div>
        <div className="notifications m-6 mb-8 py-8 pb-5 px-10">
          <div>
            <h1 className="text-3xl font-bold mb-5 text-indigo-600">
              Notifications
            </h1>
          </div>
          <div className="flex items-center mb-10">
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
          <div className="w-full lists">
            <div className="w-full flex items-center border-solid border rounded-lg px-5 py-2 my-3">
              <div className="pb-10 mr-3 p-2">
                <IoIosNotificationsOutline className='text-4xl text-indigo-600 border-indigo-600 border rounded-full' />
              </div>
              <div className="ml-2 w-full">
                <h2 className="font-bold text-xl mb-3">
                  {" "}
                  "A large transaction of $X has been made"
                </h2>
                <h2 className="px-4 py-0.5 text-white rounded-lg bg-indigo-600 text-sm">
                  12 March 2023
                </h2>
                <p>
                  <>~ </>Times of India
                </p>
              </div>
            </div>
            <div className="w-full flex items-center border-solid border rounded-lg px-5 py-2 my-3">
              <div className="pb-10 mr-3 p-2">
                <IoIosNotificationsOutline className='text-4xl text-indigo-600 border-indigo-600 border rounded-full' />
              </div>
              <div className="ml-2 w-full">
                <h2 className="font-bold text-xl mb-3">
                  {" "}
                  "A large transaction of $X has been made"
                </h2>
                <h2 className="px-4 py-0.5 text-white rounded-lg bg-indigo-600 text-sm">
                  12 March 2023
                </h2>
                <p>
                  <>~ </>Times of India
                </p>
              </div>
            </div>
            <div className="w-full flex items-center border-solid border rounded-lg px-5 py-2 my-3">
              <div className="pb-10 mr-3 p-2">
                <IoIosNotificationsOutline className='text-4xl text-indigo-600 border-indigo-600 border rounded-full' />
              </div>
              <div className="ml-2 w-full">
                <h2 className="font-bold text-xl mb-3">
                  {" "}
                  "A large transaction of $X has been made"
                </h2>
                <h2 className="px-4 py-0.5 text-white rounded-lg bg-indigo-600 text-sm">
                  12 March 2023
                </h2>
                <p>
                  <>~ </>Times of India
                </p>
              </div>
            </div>
            <div className="w-full flex items-center border-solid border rounded-lg px-5 py-2 my-3">
              <div className="pb-10 mr-3 p-2">
                <IoIosNotificationsOutline className='text-4xl text-indigo-600 border-indigo-600 border rounded-full' />
              </div>
              <div className="ml-2 w-full">
                <h2 className="font-bold text-xl mb-3">
                  {" "}
                  "A large transaction of $X has been made"
                </h2>
                <h2 className="px-4 py-0.5 text-white rounded-lg bg-indigo-600 text-sm">
                  12 March 2023
                </h2>
                <p>
                  <>~ </>Times of India
                </p>
              </div>
            </div>
            <div className="w-full flex items-center border-solid border rounded-lg px-5 py-2 my-3">
              <div className="pb-10 mr-3 p-2">
                <IoIosNotificationsOutline className='text-4xl text-indigo-600 border-indigo-600 border rounded-full' />
              </div>
              <div className="ml-2 w-full">
                <h2 className="font-bold text-xl mb-3">
                  {" "}
                  "A large transaction of $X has been made"
                </h2>
                <h2 className="px-4 py-0.5 text-white rounded-lg bg-indigo-600 text-sm">
                  12 March 2023
                </h2>
                <p>
                  <>~ </>Times of India
                </p>
              </div>
            </div>
            <div className="w-full flex items-center border-solid border rounded-lg px-5 py-2 my-3">
              <div className="pb-10 mr-3 p-2">
                <IoIosNotificationsOutline className='text-4xl text-indigo-600 border-indigo-600 border rounded-full' />
              </div>
              <div className="ml-2 w-full">
                <h2 className="font-bold text-xl mb-3">
                  {" "}
                  "A large transaction of $X has been made"
                </h2>
                <h2 className="px-4 py-0.5 text-white rounded-lg bg-indigo-600 text-sm">
                  12 March 2023
                </h2>
                <p>
                  <>~ </>Times of India
                </p>
              </div>
            </div>
            <div className="w-full flex items-center border-solid border rounded-lg px-5 py-2 my-3">
              <div className="pb-10 mr-3 p-2">
                <IoIosNotificationsOutline className='text-4xl text-indigo-600 border-indigo-600 border rounded-full' />
              </div>
              <div className="ml-2 w-full">
                <h2 className="font-bold text-xl mb-3">
                  {" "}
                  "A large transaction of $X has been made"
                </h2>
                <h2 className="px-4 py-0.5 text-white rounded-lg bg-indigo-600 text-sm">
                  12 March 2023
                </h2>
                <p>
                  <>~ </>Times of India
                </p>
              </div>
            </div>
            <div className="w-full flex items-center border-solid border rounded-lg px-5 py-2 my-3">
              <div className="pb-10 mr-3 p-2">
                <IoIosNotificationsOutline className='text-4xl text-indigo-600 border-indigo-600 border rounded-full' />
              </div>
              <div className="ml-2 w-full">
                <h2 className="font-bold text-xl mb-3">
                  {" "}
                  "A large transaction of $X has been made"
                </h2>
                <h2 className="px-4 py-0.5 text-white rounded-lg bg-indigo-600 text-sm">
                  12 March 2023
                </h2>
                <p>
                  <>~ </>Times of India
                </p>
              </div>
            </div>

          </div>
        </div>
      </div>
    </>
  );
};

export default NotificationPage;
