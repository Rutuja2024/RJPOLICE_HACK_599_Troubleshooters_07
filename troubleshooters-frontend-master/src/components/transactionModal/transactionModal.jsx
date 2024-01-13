import "./transactionModal.css";
import { IoCloseOutline } from "react-icons/io5";
import { BsUpload } from "react-icons/bs";
// import { IoCloseOutline } from "react-icons/io5";
const transactionModal = ({ closeCallback }) => {
  return (
    <div className="main-container">
      <div className="card">
        <div className="flex items-center border-solid border rounded px-5 py-2 my-2">
          <div className="text-lg font-bold bg-indigo-600 text-white rounded-full p-3">
            <BsUpload />
          </div>
          <div className="ml-5">
            <h2 className="font-bold text-md">13 January 2023</h2>
            <h2 className="text-gray-500">Amount Credited : 6000</h2>
          </div>
          <div className="ml-24 flex gap-3">
            <p className="px-3 py-1 bg-indigo-600 rounded-lg text-white text-md">
              Not Fraud
            </p>
            <div>
              <div onClick={closeCallback}>
                <IoCloseOutline className="text-indigo-600 text-2xl mr-3" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default transactionModal;
