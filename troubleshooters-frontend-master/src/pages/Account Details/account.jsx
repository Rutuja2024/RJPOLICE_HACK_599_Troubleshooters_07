import { MdAccountBalanceWallet } from "react-icons/md";
import "./account.css";
import Sidebar from "../../components/sidebar/sidebar";
import Chart from "../../components/chart/chart";
import { BsUpload } from "react-icons/bs";
import { BsDownload } from "react-icons/bs";
import { useState } from "react";
import TransactionModal from "../../components/transactionModal/transactionModal";
const Account = () => {
  const [isTransactionModalOpen, setIsTransactionModalOpen] = useState(false);

  const handleToggleTransactionModal = () => {
    setIsTransactionModalOpen(!isTransactionModalOpen);
  };
  return (
    <>
      <div className="main-div">
        <div>
          <Sidebar className="w-96" />
        </div>
        <div className="profile-main px-6 py-2 my-4 mx-5 mb-8 ml-8">
          <div>
            <h1 className="text-xl font-semibold mx-6 mt-3 mb-5 bg-indigo-600 text-white px-3 py-1 rounded-lg text-center">
              Account Details
            </h1>
          </div>
          <div className="profile-div mx-5 my-3 px-3 py-2">
            <div className="profile-img rounded-lg p-2">
              {" "}
              <img
                className="profile"
                src="https://images.unsplash.com/photo-1547425260-76bcadfb4f2c?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                alt="Your Company"
              />
            </div>
            <div className="ml-8">
              <h1 className="text-2xl font-semibold text-indigo-600 mb-3">
                Vikas Kumar
              </h1>
              <p className="bg-red-500 text-white px-8 py-1 rounded-full text-center">
                Fraudulent
              </p>
            </div>
          </div>
          <div className="mx-6 my-0">
            <h1 className="border border-indigo-600 rounded-md py-2 px-3 mb-1">
              <strong>Account Number : </strong>12458693254
            </h1>
            <h1 className="border border-indigo-600 rounded-md py-2 px-3 mb-1">
              <strong>IFSC Number : </strong>JIDH0000002
            </h1>
            <h1 className="border border-indigo-600 rounded-md py-2 px-3 mb-1">
              <strong>Branch Name : </strong>Nashik Road
            </h1>
            <h1 className="border border-indigo-600 rounded-md py-2 px-3 mb-1">
              <strong>Date of Birth : </strong>04/12/2002
            </h1>
            <h1 className="border border-indigo-600 rounded-md py-2 px-3 mb-1">
              {" "}
              <strong>Gender : </strong>Male
            </h1>
            <h1 className="border border-indigo-600 rounded-md py-2 px-3 mb-1">
              {" "}
              <strong>Mobile Number : </strong>9526598741
            </h1>
            <h1 className="border border-indigo-600 rounded-md py-2 px-3 mb-1">
              {" "}
              <strong>Email : </strong>abcz@kdf.com
            </h1>
            <h1 className="border border-indigo-600 rounded-md py-2 px-3 mb-1">
              {" "}
              <strong>Aadhaar Number : </strong>45874563281564
            </h1>
            <h1 className="border border-indigo-600 rounded-md py-2 px-3 mb-1">
              {" "}
              <strong>Pancard : </strong>FSGJ44474JD
            </h1>
          </div>
        </div>
        <div>
          <div className=" chart px-10 py-1  m-5 mt-4 mb-3">
            <Chart />
          </div>
          <div className="transactions-div px-10 py-5 m-5 mb-8">
            <div>
              <h1 className="text-2xl font-bold mb-5 text-indigo-600">
                Transaction History
              </h1>
            </div>
            <div className="transactions">
              <div
                onClick={handleToggleTransactionModal}
                className="flex items-center border-solid border rounded px-5 py-2 my-2"
              >
                <div className="text-lg font-bold bg-indigo-600 text-white rounded-full p-3">
                  <BsUpload />
                </div>
                <div className="ml-5">
                  <h2 className="font-bold text-md">13 January 2023</h2>
                  <h2 className="text-gray-500">Amount Credited : 6000</h2>
                </div>
                <div className="ml-24">
                  <p className="px-3 py-1 bg-indigo-600 rounded-lg text-white text-md">
                    Not Fraud
                  </p>
                </div>
              </div>
              <div onClick={handleToggleTransactionModal} className="flex items-center border-solid border rounded px-5 py-2 my-2">
                <div className="text-lg font-bold bg-indigo-600 text-white rounded-full p-3">
                  <BsUpload />
                </div>
                <div className="ml-5">
                  <h2 className="font-bold text-md">13 January 2023</h2>
                  <h2 className="text-gray-500">Amount Credited : 6000</h2>
                </div>
                <div className="ml-24">
                  <p className="px-3 py-1 bg-indigo-600 rounded-lg text-white text-md">
                    Not Fraud
                  </p>
                </div>
              </div>
              <div onClick={handleToggleTransactionModal} className="flex items-center border-solid border rounded px-5 py-2 my-2">
                <div className="text-lg font-bold bg-indigo-600 text-white rounded-full p-3">
                  <BsUpload />
                </div>
                <div className="ml-5">
                  <h2 className="font-bold text-md">13 January 2023</h2>
                  <h2 className="text-gray-500">Amount Credited : 6000</h2>
                </div>
                <div className="ml-24">
                  <p className="px-3 py-1 bg-indigo-600 rounded-lg text-white text-md">
                    Not Fraud
                  </p>
                </div>
              </div>
              <div onClick={handleToggleTransactionModal} className="flex items-center border-solid border rounded px-5 py-2 my-2">
                <div className="text-lg font-bold bg-indigo-600 text-white rounded-full p-3">
                  <BsUpload />
                </div>
                <div className="ml-5">
                  <h2 className="font-bold text-md">13 January 2023</h2>
                  <h2 className="text-gray-500">Amount Credited : 6000</h2>
                </div>
                <div className="ml-24">
                  <p className="px-3 py-1 bg-indigo-600 rounded-lg text-white text-md">
                    Not Fraud
                  </p>
                </div>
              </div>
              <div onClick={handleToggleTransactionModal} className="flex items-center border-solid border rounded px-5 py-2 my-2">
                <div className="text-lg font-bold bg-indigo-600 text-white rounded-full p-3">
                  <BsUpload />
                </div>
                <div className="ml-5">
                  <h2 className="font-bold text-md">13 January 2023</h2>
                  <h2 className="text-gray-500">Amount Credited : 6000</h2>
                </div>
                <div className="ml-24">
                  <p className="px-3 py-1 bg-indigo-600 rounded-lg text-white text-md">
                    Not Fraud
                  </p>
                </div>
              </div>
              <div onClick={handleToggleTransactionModal} className="flex items-center border-solid border rounded px-5 py-2 my-2">
                <div className="text-lg font-bold bg-indigo-600 text-white rounded-full p-3">
                  <BsUpload />
                </div>
                <div className="ml-5">
                  <h2 className="font-bold text-md">13 January 2023</h2>
                  <h2 className="text-gray-500">Amount Credited : 6000</h2>
                </div>
                <div className="ml-24">
                  <p className="px-3 py-1 bg-indigo-600 rounded-lg text-white text-md">
                    Not Fraud
                  </p>
                </div>
              </div>
              <div onClick={handleToggleTransactionModal} className="flex items-center border-solid border rounded px-5 py-2 my-2">
                <div className="text-lg font-bold bg-indigo-600 text-white rounded-full p-3">
                  <BsUpload />
                </div>
                <div className="ml-5">
                  <h2 className="font-bold text-md">13 January 2023</h2>
                  <h2 className="text-gray-500">Amount Credited : 6000</h2>
                </div>
                <div className="ml-24">
                  <p className="px-3 py-1 bg-indigo-600 rounded-lg text-white text-md">
                    Not Fraud
                  </p>
                </div>
              </div>
              <div onClick={handleToggleTransactionModal} className="flex items-center border-solid border rounded px-5 py-2 my-2">
                <div className="text-lg font-bold bg-indigo-600 text-white rounded-full p-3">
                  <BsUpload />
                </div>
                <div className="ml-5">
                  <h2 className="font-bold text-md">13 January 2023</h2>
                  <h2 className="text-gray-500">Amount Credited : 6000</h2>
                </div>
                <div className="ml-24">
                  <p className="px-3 py-1 bg-indigo-600 rounded-lg text-white text-md">
                    Not Fraud
                  </p>
                </div>
              </div>
              {isTransactionModalOpen ? (
                <TransactionModal
                  closeCallback={handleToggleTransactionModal}
                />
              ) : null}
            </div>
          </div>
        </div>
      </div>
    </>
  );
};
export default Account;
