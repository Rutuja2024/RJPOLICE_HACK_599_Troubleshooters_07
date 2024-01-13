const AccountNumberForm = () => {
    return (
      <>
        <div className="h-80 px-8 flex items-center justify-center w-96 mx-auto my-auto">
          <form>
            <div>
              <h1 className="text-2xl text-indigo-600 font-bold mb-8">
                Check Account Number
              </h1>
              {/* <hr className='w-32 h-1 rounded-lg bg-black'/> */}
            </div>
            <div className="flex-column">
              <h2 className="text-lg font-semibold mb-2">Account Number</h2>
              <input
                className="px-5 py-2 border rounded-lg border-indigo-600 w-72"
                placeholder="Enter Account Number"
                required
              />
            </div>
            <div>
              <button className="mt-8 bg-indigo-600 px-5 w-72 text-white rounded-lg py-2">
                Check
              </button>
            </div>
            <div>
              <p className=" text-center italic text-gray-500 mt-5">
                This Account Number is verified and secure
              </p>
            </div>
          </form>
        </div>
      </>
    );
  };
  export default AccountNumberForm;
  