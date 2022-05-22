// const API_KEY = process.env.NEXT_PUBLIC_PEXELS_API_KEY;

export const getCuratedPhotos = async () => {
	const res = await fetch(
		`https://www.reddit.com/r/images/top.json?limit=100&t=month`
	);
	const responseJson = await res.json();

	return responseJson.data.children;
};
