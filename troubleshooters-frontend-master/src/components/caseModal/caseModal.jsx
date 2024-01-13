import "./caseModal.css";
import { IoCloseOutline } from "react-icons/io5";
const caseModal = ({ closeCallback }) => {
  return (
    <div className="main-container">
      <div className='card'>
        <div className="h-48 w-full flex items-center border-solid border rounded-lg px-5 py-2 my-3 ">
          <div className="ml-2 w-full">
            <div className="flex mt-2 items-center">
              <h2 className="font-bold text-xl mb-2 "> 3594HD3294JDJ243</h2>
              <p className="ml-3 mb-1 text-white px-6 text-center text-sm pb-1 font-semibold bg-red-600 rounded-full">
                Open
              </p>
            </div>
            <p>
              <strong>Victim Name : </strong>Vikas Kumar
            </p>
            <p>
              <strong>Customer ID : </strong>DH76HNDH349239
            </p>
            <p>
              <strong>Transaction ID : </strong>DH76HNDH349239
            </p>
            <p>
              <strong>Customer ID : </strong>DH76HNDH349239
            </p>
            <h2 className="mt-2 text-sm font-semibold text-gray-600">
              12 March 2023
            </h2>
          </div>
          <div className="flex items-center justify-center pb-28 ">
            <div onClick={closeCallback}>
              <IoCloseOutline className="text-indigo-600 text-2xl mr-3" />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default caseModal;
