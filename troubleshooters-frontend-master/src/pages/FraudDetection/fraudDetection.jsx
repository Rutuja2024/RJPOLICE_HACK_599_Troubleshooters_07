import { useState } from "react";
import UpiForm from "../../components/forms/upiForm/upiForm";
import SmsForm from "../../components/forms/sms/smsForm";
import AccountNumberForm from "../../components/forms/acccountNumber/accountNumber";
import UrlForm from "../../components/forms/urlForm/urlForm";
import PhoneNumberForm from "../../components/forms/phoneNumber/phoneNumber";
import "./fraudDetection.css";
const FraudDetection = () => {
  const [formNumber, setFormNumber] = useState(1);

  const getNavItemClass = (navItem) => {
    return formNumber === navItem ? "active" : "";
  };

  return (
    <>
      <div>
        <div>
          <div className="nav flex items-center justify-between px-40 py-5 mx-5 my-2 rounded-lg">
            <div
              onClick={() => {
                console.log(formNumber);
                setFormNumber(1);
              }}
              className={`cursor-pointer min-w-48 text-center ${getNavItemClass(
                1
              )} bg-indigo-600 px-2 py-3 text-md font-semibold text-white rounded-lg hover:bg-indigo-300`}
            >
              <h2>UPI ID</h2>
            </div>

            <div
              onClick={() => {
                console.log(formNumber);
                setFormNumber(2);
              }}
              className={`cursor-pointer min-w-48 text-center ${getNavItemClass(
                2
              )} bg-indigo-600 px-2 py-3 text-md font-semibold text-white rounded-lg hover:bg-indigo-300`}
            >
              <h2>Account Number</h2>
            </div>
            <div
              onClick={() => {
                console.log(formNumber);
                setFormNumber(3);
              }}
              className={`cursor-pointer min-w-48 text-center ${getNavItemClass(
                3
              )} bg-indigo-600 px-2 py-3 text-md font-semibold text-white rounded-lg hover:bg-indigo-300`}
            >
              <h2>URL</h2>
            </div>
            <div
              onClick={() => {
                console.log(formNumber);
                setFormNumber(4);
              }}
              className={`cursor-pointer min-w-48 text-center ${getNavItemClass(
                4
              )} bg-indigo-600 px-2 py-3 text-md font-semibold text-white rounded-lg hover:bg-indigo-300`}
            >
              <h2>Phone Number</h2>
            </div>
            <div
              onClick={() => {
                console.log(formNumber);
                setFormNumber(5);
              }}
              className={`cursor-pointer min-w-48 text-center ${getNavItemClass(
                5
              )} bg-indigo-600 px-2 py-3 text-md font-semibold text-white rounded-lg hover:bg-indigo-300`}
            >
              <h2>SMS Template</h2>
            </div>
          </div>
        </div>
        <div className="rounded-2xl m-5 w-2/4 py-8 mx-auto mt-16 border border-indigo-600">
          {formNumber === 1 ? <UpiForm /> : null}
          {formNumber === 2 ? <AccountNumberForm /> : null}
          {formNumber === 3 ? <UrlForm /> : null}
          {formNumber === 4 ? <PhoneNumberForm /> : null}
          {formNumber === 5 ? <SmsForm /> : null}
        </div>
      </div>
    </>
  );
};
export default FraudDetection;
